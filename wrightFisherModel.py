# Population Sample Setup biallelic, 2 gene setup
# (Aa, Bb)
# Capital Letter(A, B) = Dominant Allele
# Small Case Letter(a, b) = Recessive Allele
import random
import matplotlib.pyplot as plt     

# Sample_1 = [("A", "a"), ("B", "b")]

# Sample_2 =  [("a", "a"), ("b", "b")]

GenerationSize = 10

Generations = 100

# Generate an allele population from the freq. of the previous
# Allele population 
def AllelePopulationGenerator(Freq_A, Freq_a, Freq_B, Freq_b, generation_size):
    Allele_A = random.choices(['A', 'a'], [Freq_A, Freq_a], k=generation_size*2)
    Allele_B = random.choices(['B', 'b'], [Freq_B, Freq_b], k=generation_size*2)
    return  Allele_A, Allele_B

def CreateGene(allele1, allele2): # Arrange the dominant allele first 

    if allele1.isupper() == allele2.isupper(): #Case 1 Homozygosity
        return (allele1, allele2)
    
    elif allele1.isupper() == True: #Case 2 Heterozygosity
        return (allele1, allele2)

    else:# Case 2 continuation
        return (allele2, allele1)


def PopulationGenerator(Alleles_A, Alleles_B): #Create a population spread from the given allele spread
    output = []
    for i in range (0, (GenerationSize*2), 2):
        geneA = CreateGene(Alleles_A[i], Alleles_A[i+1])
        geneB = CreateGene(Alleles_B[i], Alleles_B[i+1])
        output.append((geneA, geneB))
    return output


def AlleleCounter(Population): # Create a count of the alleles in population
    count_A = 0 
    count_a = 0 
    count_B = 0
    count_b = 0
    for sample in Population:
        for gene in sample:
            for allele in gene:
                if allele == "A":
                    count_A = count_A + 1
                elif allele == "a":
                    count_a = count_a + 1
                elif allele == "B":
                    count_B = count_B + 1
                elif allele == "b":
                    count_b = count_b + 1
    
    return count_A, count_a, count_B, count_b

def AlleleFrequencyGenerator(A, a, B, b):
    Freq_A = A/(A+a)
    Freq_a = a/(A+a)
    Freq_B = B/(B+b)
    Freq_b = b/(B+b)

    return Freq_A, Freq_a, Freq_B, Freq_b

# def Phenotype_Finder:

#Final Product
def WrightFisherModel(InitialPopulation, Generations_run):
    GenerationSize = len(InitialPopulation)
    Offsprings = InitialPopulation

    List_A = []
    List_a = []
    List_B = []
    List_b = []

    for i in range(Generations_run):

        #Count and create allelic frequency
        countA, counta, countB, countb = AlleleCounter(Offsprings)

        A, a, B, b = AlleleFrequencyGenerator(countA, counta, countB, countb)
        
        #Store values of the frequencies for plotting
        List_A.append(A)
        List_a.append(a)
        List_B.append(B)
        List_b.append(b)

        #Generate the next generation of samples
        AllelesA, AllelesB = AllelePopulationGenerator(A, a, B, b, GenerationSize)
        Offsprings = PopulationGenerator(AllelesA, AllelesB)
    
    print (f"\nFrequencies of A = {List_A}")
    print (f"\nFrequencies of a = {List_a}")
    print (f"\nFrequencies of B = {List_B}")
    print (f"\nFrequencies of b = {List_b}")
    print (f"\n{Offsprings}")

    return List_A, List_a, List_B, List_b

def main():

    A, B = AllelePopulationGenerator(0.5, 0.5, 0.5, 0.5, GenerationSize)
    A, a, B, b = WrightFisherModel((PopulationGenerator(A, B)), Generations)
    
    fig, ax = plt.subplots()
    
    ax.plot(A, color = 'red', label = 'Frequency of A')
    ax.plot(a, color = 'yellow', label = 'Frequency of a')
    ax.plot(B, color = 'green', label = 'Frequency of B')
    ax.plot(b, color = 'purple', label = 'Frequency of b')
    ax.legend(loc = 'upper left')
    plt.xlabel = "Generations"
    plt.ylabel = "Frequency"
    plt.show()

if __name__ == "__main__":
    main()
