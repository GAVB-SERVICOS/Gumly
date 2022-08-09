from gumly.checkpoint_flow import LocalStateHandler, CheckpointFlow
import tempfile


def test_local_state_handler():
        with tempfile.NamedTemporaryFile() as tmp_file:
                handler = LocalStateHandler(tmp_file.name) #_init_
                initial_state = handler.read()
                assert initial_state==dict()
                handler.write({'a':1, 'b':2})
                handler_= LocalStateHandler(tmp_file.name)
                initial_state = handler_.read()
                assert initial_state== {'a':1, 'b':2}

def test_CheckpointFlow():
      pass
                
    


