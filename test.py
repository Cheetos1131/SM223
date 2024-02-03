import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon, norm

r = 2
c = 2
beta = [0.5, 1, 2, 4]
n = r*c
p = norm.pdf(beta)

my_exp_data = [1.86460822e+00, 2.14303480e+00, 7.34146234e-01, 6.54052168e+00,
 1.53539195e+00, 2.15547160e+00, 1.47604160e+01, 2.78047567e+00,
 1.54664268e+00, 2.73695174e+00, 5.37323410e-01, 1.07690926e+00,
 3.72891527e+00, 1.04056286e+00, 1.28703300e+00, 2.36298272e+00,
 4.09535284e-01, 1.41434837e-01, 1.94726777e+00, 1.83767980e+00,
 4.07191544e+00, 1.08164421e-01, 1.68359395e+00, 1.03951368e+00,
 3.24417089e+00, 3.07769843e+00, 3.01658760e+00, 1.94201209e-01,
 6.39713545e+00, 3.71531649e+00, 6.34016333e-01, 1.29828052e+00,
 1.29844972e+00, 2.12763995e+00, 4.48915436e-01, 9.40592498e-01,
 6.53147368e-01, 7.85419508e-01, 1.63754151e+00, 3.93801316e+00,
 5.91096689e+00, 1.21302725e+00, 1.25363865e+00, 5.23742369e+00,
 2.72906048e-01, 3.88293238e-01, 1.26141355e+00, 5.85927205e+00,
 1.72934137e+00, 2.94743489e-03, 8.44588396e-02, 1.09658899e+00,
 2.55009361e+00, 3.21184594e+00, 2.05923156e+00, 1.94260456e-01,
 1.21460765e+00, 4.59743584e-01, 2.42704244e+00, 4.76243487e-01,
 6.17142636e-02, 7.02617627e-02, 5.78125635e-01, 4.78452233e-01,
 1.37472537e+00, 1.95082874e+00, 4.93150440e-01, 3.51437304e+00,
 3.79806420e-01, 2.95770670e+00, 3.40655333e-01, 2.78832988e+00,
 3.09990586e+00, 1.15844491e+00, 7.08409864e-01, 7.27706390e-01,
 1.67529983e+00, 1.09085582e+00, 4.30879714e-02, 2.33531012e-02,
 3.08125639e-02, 5.01669907e+00, 5.41449395e+00, 5.57730790e-02,
 7.24442607e+00, 1.92165631e+00, 2.15419170e+00, 1.10183973e+00,
 2.22875119e-01, 1.74714676e+00, 3.96621873e-01, 1.02090391e+01,
 2.74734474e+00, 6.10594344e-01, 1.21882349e+00, 1.72193033e+00,
 4.86843007e-01, 5.84929463e-01, 1.86511659e+00, 4.34551090e-02,
 5.67273753e-01, 1.80961186e+00, 1.35952576e+00, 1.05097888e-01,
 9.68733325e-01, 4.11726127e-01, 1.32210765e+00, 5.48277485e-02,
 2.35811029e+00, 1.29927671e+00, 3.17964526e+00, 3.64962744e+00,
 4.50947319e+00, 2.13188686e-01, 4.27848965e+00, 9.14194538e-01,
 1.79277203e+00, 3.05929650e-01, 1.24200463e+00, 6.14246627e-02,
 3.52754107e+00, 4.55081812e+00, 2.83811914e-01, 5.39387674e+00,
 1.04832013e-01, 3.39365206e-01, 1.40769175e-01, 2.38857911e-01,
 6.24265731e+00, 6.09348537e-01, 4.47385461e-01, 2.35674002e+00,
 3.89500327e+00, 3.61150995e-01, 5.14201649e-01, 9.08220585e-01,
 3.48305660e+00, 2.85899451e-01, 2.19894983e-01, 1.71721675e+00,
 1.02152512e+00, 4.98662668e+00, 4.46535706e+00, 2.48511985e+00,
 3.33445877e+00, 4.18347425e-01, 2.04787670e+00, 2.42086436e+00,
 2.66664542e+00, 6.57488917e+00, 5.02966283e+00, 2.99679419e-01,
 8.86494934e-01, 2.38074116e+00, 9.38115700e-01, 2.21985115e+00,
 1.07804446e+00, 4.21828365e+00, 7.84706173e-01, 7.07295010e-02,
 9.39211064e-01, 2.71065966e+00, 1.03538765e+00, 5.95800357e-01,
 5.16890264e+00, 2.58439639e+00, 4.62183376e-01, 2.13317672e-02,
 1.96774569e+00, 5.08287399e-01, 3.50698938e-01, 4.10351583e-01,
 1.85725780e+00, 1.14079541e-01, 4.68072825e-01, 3.01690829e+00,
 2.70572856e-02, 1.20070729e+00, 3.29518069e-01, 9.85593774e-01,
 1.88690544e+00, 7.65451886e-01, 4.22309274e+00, 1.44090272e+00,
 4.62601872e+00, 1.17119905e+00, 8.89013179e+00, 1.50082840e+00,
 1.94230596e+00, 5.59101539e-02, 2.99481288e+00, 2.51889898e+00,
 4.12410236e-01, 3.15352692e+00, 6.17465658e+00, 2.92949982e+00,
 4.40471131e+00, 3.84974622e-01, 2.04193732e+00, 4.72578827e-01]

plt.figure()
plt.suptitle('Test')
for i in reversed(range(0, n)):
    plt.subplot(r, c, i+1)
    plt.title('beta = ' + str(beta[i]))
    plt.hist(my_exp_data, bins='fd', density=True)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    plt.plot(x, expon.pdf(x, scale=1/beta[i]), 'k-', lw=2)
    
plt.show()