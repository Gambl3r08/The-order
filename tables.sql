CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    description VARCHAR(255) NOT NULL,
    extras VARCHAR(255) NOT NULL,
    active INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE controller_log (
    controller_log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    controller_name VARCHAR(125) NOT NULL,
    success INTEGER NOT NULL,
    message VARCHAR(255),
    active INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sub_orders (
    sub_order_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID DEFAULT gen_random_uuid(),
    product_id UUID DEFAULT gen_random_uuid(),
    quantity INTEGER NOT NULL,
    active INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT current_timestamp,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT current_timestamp
);
