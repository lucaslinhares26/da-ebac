# código de geração do gráfico 
import matplotlib.pyplot as plt
import pandas as pd

gasolina_df = pd.read_csv('gasolina.csv')

plt.plot(gasolina_df['dia'], gasolina_df['venda'], marker='x', color='blue')

plt.xlabel('Dia')
plt.ylabel('Preço de Venda R$')
plt.title('Gasolina: Preço de Venda em R$ por dia')
plt.show()

plt.savefig('gasolina2.png', format='png')