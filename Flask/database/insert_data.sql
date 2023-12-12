-- Insert sample data into tables
INSERT INTO recipes (name, instructions) VALUES
    ('Recipe 1', 'Instructions for Recipe 1'),
    ('Recipe 2', 'Instructions for Recipe 2');

INSERT INTO ingredients (name, nutritional_info) VALUES
    ('Ingredient 1', 'Nutritional info for Ingredient 1'),
    ('Ingredient 2', 'Nutritional info for Ingredient 2');

INSERT INTO categories (name, description) VALUES
    ('Category 1', 'Description for Category 1'),
    ('Category 2', 'Description for Category 2');

-- Insert sample data into linking tables
INSERT INTO ingredient_recipe (ingredient_id, recipe_id) VALUES
    (1, 1),
    (2, 1),
    (2, 2);

INSERT INTO recipe_category (recipe_id, category_id) VALUES
    (1, 1),
    (2, 2);
