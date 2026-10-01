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