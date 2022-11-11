import numpy as np
from scipy.stats import norm

class EM_algorithm():
    def __init__(self, data, num_components):
        self.N = len(data)
        self.K = num_components
        self.data = data
        
    def initialize_params(self):
        self.MU = np.array([np.mean(self.data)]*self.K)
        self.SIGMA = np.array([np.std(self.data)]*self.K)
        self.PI = np.array([1/self.K]*self.K)
        self.components = [norm(loc = self.MU[i] , scale = self.SIGMA[i]) for i in range(self.K)]
        self.data_range = np.linspace(np.min(self.data),np.max(self.data), num = 1000)
        self.pdfs = np.array([self.components[i].pdf(x = self.data_range) for i in range(self.K)])

    def plot(self):
        plt.plot(self.data_range, self.PI@self.pdfs , '-', color = 'black', label = 'GMM density')
        plt.plot(self.data, np.zeros_like(self.data), 'o', color = 'black')
        for k in range(self.K):
            plt.plot(self.data_range, self.PI[k]*self.pdfs[k], '--', label = 'Component {}'.format(k))
        plt.title('GMM clusters')
        plt.legend()
    

        
        

