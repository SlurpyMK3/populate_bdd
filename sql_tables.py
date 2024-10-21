CREATE TABLE customer(
    id INT NOT NULL,
    country VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customer_order(
    id INT NOT NULL,
    invoice_nb INT NOT NULL,
    invoice_date date NOT NULL,
    customer_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE order_detail(
    id INT NOT NULL UNIQUE,
    quantity INT NOT NULL,
    order_id INT NOT NULL,
    product_id INT NOT NULL UNIQUE,
    PRIMARY KEY (id),
    FOREIGN KEY (order_id) REFERENCES customer_order(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE product(
    id INT NOT NULL UNIQUE,
    description VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY (id)
);