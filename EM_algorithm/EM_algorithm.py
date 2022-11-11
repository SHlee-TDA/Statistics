import numpy as np
from scipy.stats import norm

class EM_algorithm():
    def __init__(self, data, num_components):
        self.N = len(data)
        self.K = num_components
        self.data = data
        self.data_range = np.linspace(np.min(self.data)-10,np.max(self.data)+10, num = 1000)

    def initialize_params(self):
        self.MU = np.array([np.mean(self.data)]*self.K)
        self.SIGMA = np.array([np.std(self.data)]*self.K)
        self.PI = np.array([1/self.K]*self.K)
        self.components = [norm(loc = self.MU[i] , scale = self.SIGMA[i]) for i in range(self.K)]
        self.pdfs = np.array([self.components[i].pdf(x = self.data_range) for i in range(self.K)])

    def set_params(self, MU, SIGMA, PI):
        self.MU = MU
        self.SIGMA = SIGMA
        self.PI = PI
        self.components = [norm(loc = self.MU[i] , scale = self.SIGMA[i]) for i in range(self.K)]
        self.pdfs = np.array([self.components[i].pdf(x = self.data_range) for i in range(self.K)])


    def plot(self):
        plt.plot(self.data_range, self.PI@self.pdfs , '-', color = 'black', label = 'GMM density')
        plt.plot(self.data, np.zeros_like(self.data), 'o', color = 'black')
        for k in range(self.K):
            plt.plot(self.data_range, self.PI[k]*self.pdfs[k], '--', label = 'Component {}'.format(k))
        plt.title('GMM clusters')
        plt.legend()
    
    

    def E_step(self):
        def k_comp_likelihood(data, n,k, MU, SIGMA, PI):
            p = PI[k]*norm(loc = MU[k], scale = SIGMA[k]).pdf(x = data[n])
            return p

        def responsibility(data,n, k, MU, SIGMA, PI):
            r_nk = k_comp_likelihood(data, n,k, MU, SIGMA, PI)/np.sum([k_comp_likelihood(data, n,i, MU, SIGMA, PI) for i in range(K)])
            return r_nk

        self.Res = np.zeros((self.N,self.K))
        for n in range(self.N):
            for k in range(self.K):
                self.Res[n,k] = responsibility(self.data, n,k, self.MU, self.SIGMA, self.PI)
        
        return self.Res
    
    def M_step(self, Res):
        N_k = Res.sum(axis = 0)
        MU = self.data@Res / N_k
        centered_data = np.array([self.data - MU[i] for i in range(self.K)])
        VAR = np.array([(centered_data[i]*centered_data[i])@Res[:,i] for i in range(self.K)])/Res.sum(axis = 0)
        SIGMA = np.sqrt(VAR)
        PI = N_k/self.N
        self.set_params(MU, SIGMA, PI)
        

