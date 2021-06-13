# CLUSTERING

def get_elbow_plot(data, n=10):
  n_cluster = [i for i in range(1, n+1)]
  n_scores = []

  for i in range(1,n+1):
    kmeans = KMeans(n_clusters=i, random_state=42, init="k-means++").fit(data)
    n_scores.append(-kmeans.score(X))

  fig = sns.lineplot(x=n_cluster, y=n_scores)
  fig.set_xticks(range(1,n+1))
  fig.set(xlabel='Number of clusters', ylabel='Score')

  return plt.show()


def get_silhuette_scores(data, n=10):
  n_cluster = [i for i in range(2, n+1)]
  s_scores = []

  for i in range(2,n+1):
    kmeans = KMeans(n_clusters=i, random_state=42, init="k-means++")
    cluster_labels = kmeans.fit_predict(data)
    silhouette = silhouette_score(data, cluster_labels)
    s_scores.append(silhouette)

  fig = sns.lineplot(x=n_cluster, y=s_scores)
  fig.set_xticks(range(2,n+1))
  fig.set(xlabel='Number of clusters', ylabel='Score')

  return plt.show()
