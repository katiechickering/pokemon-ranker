-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `pokemon_schema` DEFAULT CHARACTER SET utf8;
USE `pokemon_schema`;

-- Create pokemons table
CREATE TABLE IF NOT EXISTS `pokemons` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,
    `rank` INT NOT NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;