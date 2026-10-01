DROP TABLE game;
DROP TABLE goal;
DROP TABLE goal_reached;


CREATE TABLE tapahtumat (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nimi VARCHAR(100) NOT NULL,
    vaikutus INT NOT NULL
);

INSERT INTO tapahtumat (nimi, vaikutus)
VALUES
('Myötätuuli', 2),
('Suora_reitti', 1),
('Hyvät_sääolosuhteet', 2),
('Nopea_lähtö', 1),
('Vähäinen_lentoliikenne', 1),
('Nopea_vaihto', 2),
('Hyvä_sää', 1);