from Crypto.Util.number import inverse, long_to_bytes

n = 7735208939848985079680614633581782274371148157293352904905313315409418467322726702848189532721490121708517697848255948254656192793679424796954743649810878292688507385952920229483776389922650388739975072587660866986603080986980359219525111589659191172937047869008331982383695605801970189336227832715706317
e = 65537
c = 5300731709583714451062905238531972160518525080858095184581839366680022995297863013911612079520115435945472004626222058696229239285358638047675780769773922795279074074633888720787195549544835291528116093909456225670152733191556650639553906195856979794273349598903501654956482056938935258794217285615471681

# calculate phi from alpertron

phi = 7735208858912013174807786153875265311232475601814043799113971819203978928431722767684674067119725000291122190443795615639597996271053342184657566093781734940605689774479814988576374248690133868658052837262849840790750991863632288857652325134901612884172359123108137383953436272360300748996608000000000000

d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
