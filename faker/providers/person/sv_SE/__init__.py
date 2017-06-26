# coding=utf-8

from __future__ import unicode_literals
from collections import OrderedDict
from .. import Provider as PersonProvider

# Data source
#
# Data for this provider comes from the following source:
# Statistiska centralbyråns - Statistics Sweden
# https://www.scb.se/en/About-us/official-statistics-of-sweden/
#
# Data was collected via queries on the SCB API to obtain to the
# top 200 most common last names, male first names and female first names
# from 1999.


class Provider(PersonProvider):

    formats = OrderedDict((
        ('{{last_name}} {{first_name_male}}', 1.0),
    ))

    formats_female = formats.copy()
    formats_male = formats.copy()

    first_names_female = OrderedDict((
        ('Agnes', 0.001745),
        ('Agneta', 0.004777),
        ('Aina', 0.002274),
        ('Alexandra', 0.002762),
        ('Alice', 0.003714),
        ('Amanda', 0.003099),
        ('Anette', 0.004177),
        ('Angelica', 0.001462),
        ('Anita', 0.008407),
        ('Ann', 0.004749),
        ('Ann-Charlotte', 0.001562),
        ('Ann-Christin', 0.001383),
        ('Ann-Mari', 0.001194),
        ('Ann-Marie', 0.001974),
        ('Anna', 0.042584),
        ('Anna-Karin', 0.001175),
        ('Anna-Lena', 0.001167),
        ('Anne', 0.002491),
        ('Anne-Marie', 0.001349),
        ('Anneli', 0.003702),
        ('Annelie', 0.001470),
        ('Annette', 0.001469),
        ('Annie', 0.001357),
        ('Annika', 0.005399),
        ('Asta', 0.001437),
        ('Astrid', 0.006047),
        ('Barbro', 0.006869),
        ('Berit', 0.004732),
        ('Birgit', 0.005225),
        ('Birgitta', 0.024532),
        ('Brita', 0.002495),
        ('Britt', 0.006330),
        ('Britt-Marie', 0.002430),
        ('Britta', 0.002882),
        ('Camilla', 0.004547),
        ('Carin', 0.001447),
        ('Carina', 0.006187),
        ('Carolina', 0.001716),
        ('Caroline', 0.004014),
        ('Catarina', 0.001216),
        ('Catharina', 0.001196),
        ('Cecilia', 0.008249),
        ('Charlotta', 0.004212),
        ('Charlotte', 0.003875),
        ('Christina', 0.013235),
        ('Christine', 0.001515),
        ('Dagmar', 0.001687),
        ('Dagny', 0.001481),
        ('Doris', 0.001518),
        ('Ebba', 0.002230),
        ('Edit', 0.001620),
        ('Eivor', 0.002205),
        ('Eleonora', 0.001731),
        ('Elin', 0.006729),
        ('Elisabet', 0.024570),
        ('Elisabeth', 0.025370),
        ('Elise', 0.001198),
        ('Ella', 0.001269),
        ('Ellen', 0.002524),
        ('Ellinor', 0.001304),
        ('Elsa', 0.006168),
        ('Elsie', 0.001302),
        ('Elvira', 0.001736),
        ('Emelie', 0.003036),
        ('Emilia', 0.002176),
        ('Emma', 0.007459),
        ('Erika', 0.003543),
        ('Ester', 0.002201),
        ('Eva', 0.026496),
        ('Evelina', 0.001930),
        ('Evy', 0.001609),
        ('Felicia', 0.001269),
        ('Frida', 0.003423),
        ('Gabriella', 0.001245),
        ('Gerd', 0.003404),
        ('Gertrud', 0.002159),
        ('Greta', 0.002604),
        ('Gudrun', 0.002700),
        ('Gun', 0.004988),
        ('Gunborg', 0.003021),
        ('Gunhild', 0.003072),
        ('Gunilla', 0.007540),
        ('Gunnel', 0.003826),
        ('Gunvor', 0.003507),
        ('Hanna', 0.005512),
        ('Harriet', 0.001441),
        ('Helen', 0.002647),
        ('Helena', 0.011208),
        ('Helene', 0.002163),
        ('Helén', 0.001202),
        ('Hillevi', 0.001214),
        ('Ida', 0.004826),
        ('Inga', 0.005928),
        ('Inga-Lill', 0.001723),
        ('Ingeborg', 0.007051),
        ('Ingegerd', 0.006428),
        ('Ingegärd', 0.004587),
        ('Ingela', 0.002701),
        ('Inger', 0.010945),
        ('Ingrid', 0.018110),
        ('Irene', 0.007176),
        ('Iris', 0.001497),
        ('Irma', 0.001313),
        ('Iréne', 0.001696),
        ('Jeanette', 0.002204),
        ('Jennie', 0.001404),
        ('Jenny', 0.006327),
        ('Jessica', 0.003248),
        ('Johanna', 0.008736),
        ('Josefin', 0.002350),
        ('Josefina', 0.001294),
        ('Josefine', 0.001891),
        ('Julia', 0.002653),
        ('Kajsa', 0.001214),
        ('Karin', 0.023977),
        ('Karolina', 0.003098),
        ('Katarina', 0.006660),
        ('Kerstin', 0.013320),
        ('Kristin', 0.001999),
        ('Kristina', 0.024482),
        ('Laila', 0.001753),
        ('Lena', 0.011317),
        ('Lilian', 0.002505),
        ('Lillemor', 0.001571),
        ('Lilly', 0.001785),
        ('Lina', 0.002062),
        ('Linda', 0.006682),
        ('Linn', 0.001229),
        ('Linnea', 0.007713),
        ('Linnéa', 0.013337),
        ('Lisa', 0.004293),
        ('Lisbeth', 0.002580),
        ('Louise', 0.006398),
        ('Lovisa', 0.003016),
        ('Madeleine', 0.002603),
        ('Magdalena', 0.002318),
        ('Maj', 0.003649),
        ('Maj-Britt', 0.002919),
        ('Maja', 0.001462),
        ('Malin', 0.006314),
        ('Margareta', 0.037908),
        ('Margaretha', 0.003602),
        ('Margit', 0.004690),
        ('Mari', 0.002098),
        ('Maria', 0.061211),
        ('Marianne', 0.013455),
        ('Marie', 0.016343),
        ('Marie-Louise', 0.001508),
        ('Marina', 0.001195),
        ('Marita', 0.002490),
        ('Martina', 0.001657),
        ('Mary', 0.001719),
        ('Matilda', 0.004324),
        ('Maud', 0.001868),
        ('Mikaela', 0.001418),
        ('Mona', 0.003072),
        ('Monica', 0.005729),
        ('Monika', 0.002778),
        ('Märta', 0.004609),
        ('Nina', 0.001820),
        ('Olivia', 0.001516),
        ('Pernilla', 0.002416),
        ('Petra', 0.001964),
        ('Pia', 0.003138),
        ('Ragnhild', 0.001655),
        ('Rebecca', 0.001585),
        ('Rebecka', 0.001631),
        ('Rose-Marie', 0.001345),
        ('Rut', 0.004635),
        ('Ruth', 0.002177),
        ('Sandra', 0.003674),
        ('Sara', 0.007473),
        ('Signe', 0.002761),
        ('Sigrid', 0.002130),
        ('Siv', 0.005860),
        ('Sofia', 0.011263),
        ('Sofie', 0.003466),
        ('Solveig', 0.002937),
        ('Sonja', 0.004030),
        ('Stina', 0.002603),
        ('Susanna', 0.001707),
        ('Susanne', 0.006845),
        ('Svea', 0.002225),
        ('Sylvia', 0.001630),
        ('Teresia', 0.001703),
        ('Therese', 0.004420),
        ('Therése', 0.001215),
        ('Ulla', 0.009528),
        ('Ulla-Britt', 0.001683),
        ('Ulrika', 0.005582),
        ('Valborg', 0.001616),
        ('Vera', 0.001495),
        ('Veronica', 0.001985),
        ('Victoria', 0.002490),
        ('Viktoria', 0.006375),
        ('Vilhelmina', 0.001311),
        ('Viola', 0.009669),
        ('Ylva', 0.001296),
        ('Yvonne', 0.004993),
        ('Åsa', 0.005076),
    ))

    first_names_male = OrderedDict((
        ('Adam', 0.001770),
        ('Albert', 0.001419),
        ('Albin', 0.001392),
        ('Alexander', 0.006474),
        ('Alf', 0.003571),
        ('Alfred', 0.001069),
        ('Allan', 0.003591),
        ('Alvar', 0.001072),
        ('Anders', 0.025312),
        ('Andreas', 0.008399),
        ('André', 0.001357),
        ('Anton', 0.002930),
        ('Arne', 0.010637),
        ('Arnold', 0.001027),
        ('Artur', 0.001269),
        ('Arvid', 0.002169),
        ('Axel', 0.006910),
        ('Bengt', 0.014569),
        ('Benny', 0.001397),
        ('Bernt', 0.002951),
        ('Bert', 0.001153),
        ('Bertil', 0.010902),
        ('Birger', 0.003109),
        ('Björn', 0.007803),
        ('Bo', 0.011988),
        ('Bror', 0.003281),
        ('Börje', 0.003853),
        ('Carl', 0.013483),
        ('Christer', 0.007964),
        ('Christian', 0.004359),
        ('Christoffer', 0.002267),
        ('Claes', 0.002743),
        ('Conny', 0.001928),
        ('Dan', 0.002910),
        ('Daniel', 0.009526),
        ('David', 0.005483),
        ('Dennis', 0.001779),
        ('Edvard', 0.001253),
        ('Edvin', 0.001559),
        ('Egon', 0.001019),
        ('Einar', 0.002486),
        ('Elias', 0.001085),
        ('Emanuel', 0.003777),
        ('Emil', 0.004770),
        ('Eric', 0.003387),
        ('Erik', 0.041018),
        ('Erland', 0.001450),
        ('Erling', 0.001173),
        ('Ernst', 0.002205),
        ('Evert', 0.003313),
        ('Filip', 0.001959),
        ('Folke', 0.002876),
        ('Fredrik', 0.011770),
        ('Georg', 0.003446),
        ('Gerhard', 0.001174),
        ('Gert', 0.001548),
        ('Gunnar', 0.017957),
        ('Gustaf', 0.007420),
        ('Gustav', 0.009406),
        ('Göran', 0.012287),
        ('Gösta', 0.005590),
        ('Göte', 0.002297),
        ('Hans', 0.016636),
        ('Harald', 0.002359),
        ('Harry', 0.002872),
        ('Helge', 0.002005),
        ('Henning', 0.001194),
        ('Henrik', 0.007644),
        ('Henry', 0.003134),
        ('Herbert', 0.001257),
        ('Hjalmar', 0.001179),
        ('Holger', 0.001641),
        ('Hugo', 0.001976),
        ('Håkan', 0.006974),
        ('Inge', 0.002880),
        ('Ingemar', 0.009024),
        ('Ingmar', 0.001138),
        ('Ingvar', 0.006758),
        ('Ivan', 0.001668),
        ('Ivar', 0.002943),
        ('Jacob', 0.001023),
        ('Jakob', 0.001299),
        ('Jan', 0.017300),
        ('Jan-Erik', 0.001094),
        ('Jens', 0.002221),
        ('Jesper', 0.002177),
        ('Jimmy', 0.002120),
        ('Joakim', 0.004606),
        ('Joel', 0.001778),
        ('Johan', 0.021986),
        ('Johannes', 0.003538),
        ('John', 0.008741),
        ('Johnny', 0.001499),
        ('Jonas', 0.007433),
        ('Jonathan', 0.001616),
        ('Jonny', 0.001420),
        ('Josef', 0.001131),
        ('Juhani', 0.001368),
        ('Jörgen', 0.003869),
        ('Karl', 0.030342),
        ('Kenneth', 0.003540),
        ('Kent', 0.004156),
        ('Kim', 0.001298),
        ('Kjell', 0.007932),
        ('Klas', 0.001989),
        ('Knut', 0.002668),
        ('Krister', 0.002433),
        ('Kristian', 0.001849),
        ('Kristoffer', 0.001548),
        ('Kurt', 0.004453),
        ('Lars', 0.031620),
        ('Lars-erik', 0.001056),
        ('Leif', 0.009180),
        ('Lennart', 0.019721),
        ('Linus', 0.001817),
        ('Ludvig', 0.001014),
        ('Magnus', 0.009301),
        ('Marcus', 0.004065),
        ('Markus', 0.002075),
        ('Martin', 0.008861),
        ('Mathias', 0.001551),
        ('Mats', 0.008403),
        ('Mattias', 0.005657),
        ('Max', 0.001234),
        ('Michael', 0.004456),
        ('Mikael', 0.015583),
        ('Morgan', 0.001377),
        ('Nicklas', 0.001201),
        ('Niclas', 0.001643),
        ('Niklas', 0.003704),
        ('Nils', 0.018831),
        ('Ola', 0.002691),
        ('Olle', 0.001666),
        ('Olof', 0.017132),
        ('Olov', 0.005457),
        ('Oscar', 0.002606),
        ('Oskar', 0.005198),
        ('Otto', 0.001361),
        ('Ove', 0.004994),
        ('Patrik', 0.005091),
        ('Paul', 0.002455),
        ('Per', 0.022690),
        ('Peter', 0.014015),
        ('Petter', 0.001150),
        ('Philip', 0.001340),
        ('Pierre', 0.001014),
        ('Pontus', 0.001652),
        ('Pär', 0.002043),
        ('Ragnar', 0.002983),
        ('Rasmus', 0.001323),
        ('Reinhold', 0.001075),
        ('Richard', 0.002053),
        ('Rickard', 0.002830),
        ('Rikard', 0.001272),
        ('Robert', 0.006959),
        ('Robin', 0.003012),
        ('Roger', 0.005033),
        ('Roland', 0.006879),
        ('Rolf', 0.007914),
        ('Ronny', 0.001561),
        ('Rune', 0.005600),
        ('Samuel', 0.001473),
        ('Sebastian', 0.003275),
        ('Sigurd', 0.001099),
        ('Sigvard', 0.002438),
        ('Simon', 0.003338),
        ('Sixten', 0.001299),
        ('Staffan', 0.001627),
        ('Stefan', 0.009034),
        ('Sten', 0.003911),
        ('Stig', 0.009343),
        ('Sture', 0.002518),
        ('Sune', 0.002173),
        ('Sven', 0.017897),
        ('Sören', 0.002376),
        ('Tage', 0.002198),
        ('Thomas', 0.007380),
        ('Tobias', 0.003623),
        ('Tom', 0.000977),
        ('Tomas', 0.004168),
        ('Tommy', 0.005526),
        ('Tony', 0.001814),
        ('Torbjörn', 0.002984),
        ('Tord', 0.001449),
        ('Tore', 0.002630),
        ('Torsten', 0.002915),
        ('Ture', 0.001212),
        ('Ulf', 0.008541),
        ('Uno', 0.001812),
        ('Urban', 0.001584),
        ('Valdemar', 0.002204),
        ('Valter', 0.001371),
        ('Verner', 0.001196),
        ('Victor', 0.001543),
        ('Viktor', 0.003080),
        ('Vilhelm', 0.003785),
        ('Wilhelm', 0.002195),
        ('William', 0.002332),
        ('Yngve', 0.002698),
        ('Åke', 0.013837),
    ))

    first_names = first_names_male.copy()
    first_names.update(first_names_female)

    last_names = OrderedDict((
        ('Abrahamsson', 0.002440),
        ('Adolfsson', 0.002012),
        ('Alm', 0.001448),
        ('Andersson', 0.074993),
        ('Andreasson', 0.002450),
        ('Aronsson', 0.001722),
        ('Arvidsson', 0.003474),
        ('Augustsson', 0.001306),
        ('Axelsson', 0.006128),
        ('Bengtsson', 0.009764),
        ('Berg', 0.005072),
        ('Berggren', 0.002914),
        ('Berglund', 0.005115),
        ('Bergman', 0.003560),
        ('Bergqvist', 0.002172),
        ('Bergström', 0.005561),
        ('Berntsson', 0.001280),
        ('Björk', 0.003265),
        ('Björklund', 0.002883),
        ('Björkman', 0.001760),
        ('Blom', 0.002326),
        ('Blomberg', 0.001464),
        ('Blomqvist', 0.002349),
        ('Boman', 0.001365),
        ('Borg', 0.001954),
        ('Boström', 0.001985),
        ('Bäckström', 0.001865),
        ('Börjesson', 0.002036),
        ('Carlsson', 0.007727),
        ('Claesson', 0.001600),
        ('Dahl', 0.002064),
        ('Dahlberg', 0.002382),
        ('Dahlgren', 0.001578),
        ('Dahlström', 0.001538),
        ('Danielsson', 0.004208),
        ('Davidsson', 0.002035),
        ('Edlund', 0.001649),
        ('Ek', 0.002187),
        ('Ekberg', 0.001201),
        ('Eklund', 0.003919),
        ('Ekman', 0.001847),
        ('Ekström', 0.002670),
        ('Eliasson', 0.003127),
        ('Englund', 0.001958),
        ('Engström', 0.004079),
        ('Ericsson', 0.001221),
        ('Eriksson', 0.039871),
        ('Erlandsson', 0.001768),
        ('Falk', 0.002035),
        ('Forsberg', 0.004265),
        ('Forslund', 0.001137),
        ('Fransson', 0.003937),
        ('Franzén', 0.001491),
        ('Fredriksson', 0.004959),
        ('Friberg', 0.001828),
        ('Gunnarsson', 0.003764),
        ('Gustafsson', 0.020795),
        ('Gustavsson', 0.007363),
        ('Göransson', 0.002330),
        ('Haglund', 0.001575),
        ('Hagström', 0.001315),
        ('Hallberg', 0.002017),
        ('Hansen', 0.001804),
        ('Hansson', 0.012512),
        ('Hedberg', 0.001824),
        ('Hedlund', 0.002617),
        ('Hedman', 0.001419),
        ('Hedström', 0.001406),
        ('Hellberg', 0.001212),
        ('Hellström', 0.002385),
        ('Henriksson', 0.004586),
        ('Hermansson', 0.002866),
        ('Hjalmarsson', 0.001191),
        ('Holm', 0.003700),
        ('Holmberg', 0.003521),
        ('Holmgren', 0.002689),
        ('Holmqvist', 0.001561),
        ('Holmström', 0.001904),
        ('Hägglund', 0.001134),
        ('Håkansson', 0.004300),
        ('Högberg', 0.001492),
        ('Höglund', 0.001861),
        ('Isaksson', 0.003349),
        ('Ivarsson', 0.002209),
        ('Jakobsson', 0.005863),
        ('Jansson', 0.014518),
        ('Jensen', 0.001898),
        ('Johannesson', 0.001813),
        ('Johansson', 0.076124),
        ('Johnsson', 0.003881),
        ('Jonasson', 0.002439),
        ('Jonsson', 0.016550),
        ('Josefsson', 0.002104),
        ('Jönsson', 0.009781),
        ('Karlsson', 0.058698),
        ('Klasson', 0.001235),
        ('Knutsson', 0.001627),
        ('Kristiansson', 0.001226),
        ('Larsson', 0.036191),
        ('Lilja', 0.001410),
        ('Lind', 0.003910),
        ('Lindahl', 0.001815),
        ('Lindberg', 0.007056),
        ('Lindblad', 0.001253),
        ('Lindblom', 0.001864),
        ('Lindell', 0.001351),
        ('Linder', 0.001210),
        ('Lindgren', 0.006080),
        ('Lindholm', 0.002166),
        ('Lindkvist', 0.001233),
        ('Lindqvist', 0.004209),
        ('Lindström', 0.006642),
        ('Lindén', 0.001551),
        ('Ljung', 0.001232),
        ('Ljungberg', 0.001274),
        ('Lund', 0.002142),
        ('Lundberg', 0.005680),
        ('Lundgren', 0.005495),
        ('Lundin', 0.003970),
        ('Lundkvist', 0.001252),
        ('Lundmark', 0.001410),
        ('Lundqvist', 0.003493),
        ('Lundström', 0.003173),
        ('Löfgren', 0.002211),
        ('Magnusson', 0.007333),
        ('Malm', 0.001580),
        ('Malmberg', 0.001224),
        ('Martinsson', 0.002500),
        ('Mattsson', 0.004904),
        ('Melin', 0.001487),
        ('Moberg', 0.001532),
        ('Molin', 0.001312),
        ('Månsson', 0.002563),
        ('Mårtensson', 0.003432),
        ('Möller', 0.002013),
        ('Nielsen', 0.001623),
        ('Nilsson', 0.050327),
        ('Norberg', 0.002325),
        ('Nord', 0.001346),
        ('Nordin', 0.002799),
        ('Nordström', 0.003207),
        ('Norman', 0.001228),
        ('Norén', 0.001524),
        ('Nyberg', 0.003291),
        ('Nygren', 0.001880),
        ('Nyman', 0.002117),
        ('Nyström', 0.003538),
        ('Näslund', 0.001331),
        ('Ohlsson', 0.001141),
        ('Olausson', 0.001503),
        ('Olofsson', 0.006893),
        ('Olsson', 0.032427),
        ('Oskarsson', 0.001576),
        ('Ottosson', 0.002066),
        ('Palm', 0.001957),
        ('Paulsson', 0.001382),
        ('Pedersen', 0.001201),
        ('Persson', 0.031475),
        ('Petersson', 0.008913),
        ('Pettersson', 0.019276),
        ('Pålsson', 0.001626),
        ('Roos', 0.001447),
        ('Rosén', 0.001810),
        ('Samuelsson', 0.003855),
        ('Sandberg', 0.004613),
        ('Sandström', 0.002761),
        ('Sjöberg', 0.004282),
        ('Sjödin', 0.001399),
        ('Sjögren', 0.002585),
        ('Sjöström', 0.001921),
        ('Skoglund', 0.001788),
        ('Sköld', 0.001266),
        ('Stenberg', 0.001784),
        ('Strand', 0.001771),
        ('Strandberg', 0.001755),
        ('Ström', 0.002872),
        ('Strömberg', 0.002357),
        ('Ståhl', 0.001260),
        ('Sundberg', 0.002691),
        ('Sundin', 0.001434),
        ('Sundqvist', 0.001526),
        ('Sundström', 0.002302),
        ('Svensson', 0.030624),
        ('Svärd', 0.001284),
        ('Söderberg', 0.003305),
        ('Söderlund', 0.001970),
        ('Söderström', 0.002226),
        ('Törnqvist', 0.001176),
        ('Viklund', 0.001833),
        ('Vikström', 0.001757),
        ('Wahlström', 0.001139),
        ('Wallin', 0.003077),
        ('Wikström', 0.001522),
        ('Åberg', 0.002664),
        ('Ågren', 0.001320),
        ('Åkesson', 0.002344),
        ('Åström', 0.002272),
        ('Öberg', 0.002448),
        ('Öhman', 0.001415),
        ('Östlund', 0.001623)
    ))
