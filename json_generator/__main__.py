import timeit
import random
import json

def main():

    start = timeit.default_timer()

    nombres = ["Fran", "Gun", "Harmey", "Lucas", "Enzo","Rodri"]
    paises = ["Argentina","Chile","Brasil","Paraguay","Uruguay","Peru","Ecuador","Venezuela","Bolivia","Colombia","Estados unidos","Canada","Mexico","Espana","Francia","Portugal","Alemania","Noruega","Dinamarca","Finlandia","Suecia"]
    codigo = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z",0,1,2,3,4,5,6,7,8,9]
    personas = []

    for x in range(100000):

        code = random.sample(codigo, 10)
        persona = {}
        persona["Nombre"] = random.choice(nombres)
        persona["Edad"] = random.randint(1, 100)
        persona["Pais"] = random.choice(paises)
        persona["Codigo"] = ''.join([str(elem) for elem in code])

        personas.append(persona)

    with open("output.json", "w") as f:
        json.dump(personas, f, indent=2)

    print("Al programa le llevo %s segundos ejecutarse" %round(timeit.default_timer() - start))

if __name__ == '__main__':
    main()