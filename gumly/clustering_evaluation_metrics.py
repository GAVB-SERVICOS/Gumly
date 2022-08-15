from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score

silhouette_coefficients = []
calinski_coefficients = []
davies_coefficients = []
distorsions = []

def clustering_evaluation_metrics():
    x = range(2,15)
    for k in x:
        kmeans = KMeans(n_clusters=k, random_state = 1)
        kmeans.fit(df_pca)

        silhueta = silhouette_score(df_pca, kmeans.labels_)
        silhouette_coefficients.append(silhueta)

        calinski = calinski_harabasz_score(df_pca, kmeans.labels_)
        calinski_coefficients.append(calinski)

        davies = davies_bouldin_score(df_pca, kmeans.labels_)
        davies_coefficients.append(davies)

        distorcao = kmeans.inertia_
        distorsions.append(distorcao)

        # Silhueta e Calinski quanto maior melhor
        # Davies quanto menor melhor

        print("Número de clusters: {:1}  Silhueta: {:1.4}  Elbow: {:1.4}  Calinski: {:1.4}  Davies: {:1.4}".format(k, silhueta,distorcao, calinski, davies))
    fig, axs = plt.subplots(2, 2,figsize=(10,10))

# x é o vetor com os clusters para testar no laço for

    axs[0, 0].plot(x, silhouette_coefficients)
    axs[0, 0].set_title('Silhueta')
    axs[0, 1].plot(x, distorsions, 'tab:orange')
    axs[0, 1].set_title('Elbow')
    axs[1, 0].plot(x, calinski_coefficients, 'tab:green')
    axs[1, 0].set_title('Calinski Harabasz')
    axs[1, 1].plot(x, davies_coefficients, 'tab:red')
    axs[1, 1].set_title('Davies Bouldin')

    for ax in axs.flat:
        ax.set(xlabel='Clusters', ylabel='Score', xticks = x)

    for ax in axs.flat:
        ax.grid()

    return plt.show()