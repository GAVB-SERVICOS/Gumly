from gumly.checkpoint_flow import LocalStateHandler, CheckpointFlow
import tempfile
import pytest

class StepException(Exception):
  pass


def test_local_state_handler():
        with tempfile.NamedTemporaryFile() as tmp_file:
                handler = LocalStateHandler(tmp_file.name) #_init_
                initial_state = handler.read()
                assert initial_state==dict()
                handler.write({'a':1, 'b':2})
                handler_= LocalStateHandler(tmp_file.name)
                initial_state = handler_.read()
                assert initial_state== {'a':1, 'b':2}


@pytest.fixture
def fixture_checkpointflow():
    with tempfile.NamedTemporaryFile() as tmp_file:
      cp = CheckpointFlow(tmp_file.name)
      initial_state = dict(a='value of A')
      
      def loader(state):
        print("loader")
        return {'x': [1, 2, 3]}
      def saver(state, data):
        print(f"saver printing data={data}")

      @cp.add_step(load=loader, save=saver)
      def f1(state, data):
        print(f"f1 printing state: {state}")
        print(f"f1 printing data: {data}")
        state['d'] = 'D'

      yield cp, initial_state

      
def test_checkpointflow_with_error(fixture_checkpointflow):
  cp, initial_state = fixture_checkpointflow
  initial_state['break'] = True
  
  def loader3(state):
    print("loader3")
    return {'z': ['A', 'B', 'C']}

  def saver3(state, data):
    print(f"saver3 printing data={data}")

  @cp.add_step()
  def f2(state, data):
    if state['break']:
      raise StepException("This thing broke!")
  
  @cp.add_step(load=loader3, save=saver3)
  def f3(state, data):
    print(f"f3 printing state: {state}")
    print(f"f3 printing data: {data}")
    state['c'] = 4.5
  with pytest.raises(StepException) as ex:
    cp.run(initial_state) 
    assert str(ex) == "This thing broke!"
  cp_state = cp.handler.read()
  
  #Fixing f2 function
  cp_state['break'] = False
  cp.handler.write(cp_state)

  assert cp_state['checkpoint_index'] == 1
  cp.run(initial_state)
  cp_state = cp.handler.read()
  assert cp_state['checkpoint_index'] == 0


def test_checkpointflow_with_params(fixture_checkpointflow):
  cp, initial_state = fixture_checkpointflow
  def loader3(state):
    print("loader3")
    return {'z': ['A', 'B', 'C']}

  def saver3(state, data):
    print(f"saver3 printing data={data}")
  
  @cp.add_step()
  def f2(state, data):
    print(f"f2 printing state: {state}")
    print(f"f2 printing data: {data}")
    state['b'] = 5.5

  @cp.add_step(load=loader3, save=saver3)
  def f3(state, data):
    print(f"f3 printing state: {state}")
    print(f"f3 printing data: {data}")
    state['c'] = 4.5

  cp.run(initial_state, checkpoint=1)
  assert initial_state['b'] == 5.5
  cp.run(initial_state, load_policy='always')
  cp_state = cp.handler.read()
  cp.handler.write(cp_state)
  cp.run(initial_state, load_policy='always')
  cp_state = cp.handler.read()
  assert cp_state['d']== 'D'

