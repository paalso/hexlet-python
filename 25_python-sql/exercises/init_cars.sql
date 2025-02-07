DROP TABLE IF EXISTS cars;

CREATE TABLE cars(
    id SERIAL PRIMARY KEY,
    brand VARCHAR(255),
    model VARCHAR(255)
);

INSERT INTO cars (brand, model) VALUES
('lada', 'zaporozhets'), 
('cherry', '9');
