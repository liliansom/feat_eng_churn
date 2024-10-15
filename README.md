# Feature Engineering 

Feature engineering é o processo de transformar dados brutos em variáveis (features) que podem ser utilizadas por modelos de machine learning para melhorar a previsão e desempenho. Isso inclui a criação de novas features, como a extração de informações relevantes a partir de dados existentes, a transformação de dados categóricos em numéricos, a normalização de dados e a detecção e correção de valores ausentes ou discrepantes.

O objetivo deste projeto é otimizar as features para um modelo de machine learning, aumentar a precisão e a eficiência do modelo, facilitando assim a identificação de padrões importantes nos dados.

# Etapas do Processo
1. Introdução

   Explicação sobre os dados e o processo a ser realizado.
    
3. Importação das Bibliotecas

   Importação das bibliotecas que serão utilizadas no processo.
    
4. Criação do Ambiente Spark

   A criação de um ambiente Spark é o processo de configurar um ambiente de computação que utiliza o Apache Spark, um framework de processamento de dados em larga escala. Este ambiente pode incluir a instalação do Spark, configuração de variáveis de ambiente, e a integração com ferramentas como Jupyter Notebook, que permitem a interação com os dados de forma eficiente e intuitiva.

   Os motivos para a decisão de trabalhar com spark são:
    
    * Processamento Distribuído: O Apache Spark é projetado para processar grandes volumes de dados de forma distribuída, o que significa que ele pode realizar operações em paralelo em clusters de computação, resultando em maior eficiência e velocidade.
    *  Flexibilidade: O Spark suporta diversas linguagens de programação, como Python, Java, Scala e R. Isso permite que os desenvolvedores escolham a linguagem com a qual estão mais confortáveis, facilitando a integração e a implementação de soluções de dados.
    * Diversas Funcionalidades: O ambiente Spark oferece uma gama de bibliotecas e módulos, como Spark SQL, MLlib (para aprendizado de máquina), Spark Streaming (para processamento de dados em tempo real) e GraphX (para processamento de gráficos), permitindo uma variedade de aplicações em diferentes áreas.
    * Integração com Big Data: O Spark é frequentemente utilizado em conjunto com sistemas de armazenamento de dados grandes, como Hadoop, Apache Cassandra e Amazon S3, permitindo o acesso e o processamento de dados em larga escala.
    * Desempenho: O Spark é otimizado para desempenho, com características como execução em memória, o que reduz o tempo necessário para ler e escrever dados em disco. Isso o torna mais rápido em comparação com outras soluções de processamento de dados.
    * Análise de Dados Interativa: A criação de um ambiente Spark, especialmente em conjunto com ferramentas como Jupyter Notebook, facilita a análise interativa de dados. Os usuários podem executar comandos e visualizar resultados em tempo real, promovendo uma melhor exploração dos dados.        
    
6. Importação dos Dados

   Nesta etapa serão importados os dados a serem trabalhados neste notebook.
    
8. Análise Exploratória dos Dados

   A análise exploratória dos dados é a etapa em que as tabelas importadas anteriormente serão analisadas quanto ao tipo dos metadados, à quantidade de dados, aos dados faltantes, às suas distribuições, entre outras informações fundamentais para iniciar qualquer tipo de trabalho.
    
10. Tratamento dos Dados

    Nesta etapa iremos realizar a feature selection que é o processo de identificar e selecionar as características (features) mais relevantes de um conjunto de dados para a construção de um modelo de machine learning. Essa etapa é crucial no pré-processamento dos dados, pois impacta diretamente na qualidade e desempenho do modelo. Os principais motivos de realizar a feature selection são: Redução da Dimensionalidade, Melhoria da Performance do Modelo, Interpretação e Explicabilidade, Aumento da Generalização e Facilitação da Visualização.

12. Criação das Variáveis

    Nesta etapa iremos criar as variáveis explicativas e variáveis históricas.

    A cada variável criada serão realizados as seguintes etapas:

    * Criação da variável
    * Armazenamento do df em .parquet
    * Criação da função desta variável no arquivo feature_store_churn
    * Uso da função neste notebook
    
    7.1. Variáveis explicativas:

    * Tempo desde a Última Transação: A diferença entre a data mais recente no conjunto de dados e a última data de compra de cada cliente.
    * Frequência de Compra: Quantidade de compras que o cliente fez dividida pelo número de meses desde sua inscrição.
    * Total Gasto: Soma de todos os valores gastos pelo cliente em todas as suas transações.
    * Categoria Favorita: Categoria de produto em que o cliente gastou a maior quantia.
    * Gasto Médio por Transação: Total gasto dividido pelo número total de transações.
    * Duração da Assinatura: Número de dias desde que o cliente se inscreveu até a data mais recente no conjunto de dados.
    * Número de Categorias Compradas: Quantidade de categorias diferentes das quais o cliente comprou.
    * Usou Suporte antes da Primeira Compra: Indicador (1 ou 0) se o cliente usou o suporte antes de fazer sua primeira compra.
    * Dias entre Inscrição e Primeira Compra: Diferença em dias entre a data de inscrição do cliente e sua primeira transação.
    * Frequência de Transações por Plano: Número de transações do cliente dividido pelos meses de inscrição, segmentado por plano (Básico, Intermediário, Avançado)

    7.2. Variáveis históricas - 3 meses:
    
    * Média do Valor Gasto em Esportes nos Últimos 3 Meses: Esta variável calcula a média dos gastos do cliente na categoria "Esportes" nos últimos três meses.
    * Média do Valor Gasto em Eletrônicos nos Últimos 3 Meses: Semelhante à anterior, mas focada na categoria "Eletrônicos".
    * Média do Valor Gasto em Roupas nos Últimos 3 Meses: Foca na categoria "Roupas", representando a média dos gastos do cliente nos últimos três meses.
    * Média do Valor Gasto em Alimentos nos Últimos 3 Meses: Representa a média dos gastos do cliente na categoria "Alimentos" nos últimos três meses.
    * Média do Valor Gasto em Livros nos Últimos 3 Meses: Foca na categoria "Livros", calculando a média dos gastos do cliente nos últimos três meses.

    7.3. Repita o passo anterior considerando - últimos 6 meses
   
    7.4. Repita o passo anterior considerando - últimos 9 meses
   
    7.5. Repita o passo anterior considerando - últimos 12 meses

14. Criação de Novo Arquivo

    Ao final do processo, iremos gerar novos arquivos no formato .csv e .parquet.

Andamento do Projeto: Em Andamento.
