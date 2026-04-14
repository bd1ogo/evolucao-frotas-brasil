SELECT 
    ano, SUM(quantidade) AS total_veiculos
FROM frota
GROUP BY ano
ORDER BY ano;

SELECT 
    ano,
    SUM(quantidade) AS total_veiculos,
    LAG(SUM(quantidade)) OVER (ORDER BY ano) AS ano_anterior,
    ROUND(
        (
            SUM(quantidade) - LAG(SUM(quantidade)) OVER (ORDER BY ano)
        ) / LAG(SUM(quantidade)) OVER (ORDER BY ano) * 100, 2
    ) AS crescimento_percentual
FROM frota
GROUP BY ano
ORDER BY ano;

SELECT 
    estado, SUM(quantidade) AS total_veiculos
FROM frota
GROUP BY estado
ORDER BY total_veiculos DESC;

SELECT 
    tipo, SUM(quantidade) AS total
FROM frota
GROUP BY tipo
ORDER BY total DESC;