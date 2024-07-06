CREATE TABLE chatbot_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pattern VARCHAR(255) NOT NULL,
    response TEXT NOT NULL,
    precaution TEXT,
    -- Add more columns as needed
);


