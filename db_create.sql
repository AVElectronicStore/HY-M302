
CREATE TABLE switches (
                id INT NOT NULL,
                valor BOOLEAN NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE sensores (
                fecha DATETIME NOT NULL,
                humedad DECIMAL(5,2) NOT NULL,
                temperatura DECIMAL(5,2) NOT NULL,
                luz DECIMAL(5,2) NOT NULL,
                potenciometro DECIMAL(4,2) NOT NULL,
                PRIMARY KEY (fecha)
);
