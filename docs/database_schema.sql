PRAGMA foreign_keys = ON;

CREATE TABLE roles (
    id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL UNIQUE
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles (id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE manufacturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_name TEXT NOT NULL UNIQUE
);

CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL UNIQUE
);

CREATE TABLE products (
    article TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    base_price REAL NOT NULL CHECK (base_price >= 0),
    stock_count INTEGER NOT NULL CHECK (stock_count >= 0),
    discount_percent INTEGER NOT NULL CHECK (discount_percent >= 0 AND discount_percent <= 100),
    image_path TEXT,
    FOREIGN KEY (category_id) REFERENCES categories (id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
);

CREATE TABLE pickup_points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address_text TEXT NOT NULL UNIQUE
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    order_date TEXT NOT NULL,
    delivery_date TEXT NOT NULL,
    pickup_point_id INTEGER NOT NULL,
    client_name TEXT NOT NULL,
    receive_code TEXT,
    order_status TEXT NOT NULL,
    FOREIGN KEY (pickup_point_id) REFERENCES pickup_points (id)
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_article TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_article) REFERENCES products (article)
);
