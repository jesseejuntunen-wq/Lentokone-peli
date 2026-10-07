DROP TABLE game;
DROP TABLE goal;
DROP TABLE goal_reached;

CREATE TABLE pos_tapahtumat (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nimi VARCHAR(100) NOT NULL,
    vaikutus INT NOT NULL
);

INSERT INTO pos_tapahtumat (nimi, vaikutus)
VALUES
('Myötätuuli', 2),
('Suora_reitti', 1),
('Hyvät_sääolosuhteet', 2),
('Nopea_lähtö', 1),
('Vähäinen_lentoliikenne', 1),
('Nopea_vaihto', 2),
('Hyvä_sää', 1);
CREATE TABLE tapahtumat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nimi VARCHAR(50),
    aika_muutos DECIMAL(4,1)
);


INSERT INTO tapahtumat (nimi, aika_muutos)
VALUES
('pieni-myrsky', -0.2),
('pelkääntyi lintu', -2.0),
('suur-myrsky', -0.8),
('bensiini-lopussa', -0.5),
('myräkkä', -0.6);