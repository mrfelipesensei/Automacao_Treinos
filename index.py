import tkinter as tk
import random

#Grupos musculares e exercícios
exercicios = {
    'Peito': ['Crucifixo','Supino Sentado','Flexão de Braço','Flexão Declinada'],
    'Costas': ['Puxada Alta','Remada Baixa','Puxada Alta Triângulo','Remada Curvada'],
    'Quadriceps' : ['Extensora','Agachamento','Afundo','Agachamento Búlgaro'],
    'Femoral' : ['Stiff','Cadeira Flexora','Levantamento Terra'],
    'Panturrilha': ['Panturrilha em Pé','Panturrilha Sentado'],
    'Ombro': ['Desenvolvimento','Elevação Lateral','Elevação Frontal','Arnold Press'],
    'Bíceps': ['Rosca Direta','Rosca Alternada','Rosca Martelo'],
    'Tríceps': ['Tríceps Polia','Mergulho','Tríceps Testa'],
    'Antebraço': ['Rosca de Punho','Rosca Direta Invertida'],
    'Trapézio': ['Remada Alta','Encolhimento Ombro','Face Pull'],
    'Abdominal': ['Reto','Bicicleta','Rotação Russa','Prancha','Alpinista'],
    'Cárdio' : ['Corrida','Pular Corda','Funcional','Elíptico']
}

#Definindo os dias da semana para os treinos
dias_semana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado']

def gerar_estrategia():
    grupos = list(exercicios.keys()) #Cria uma lista com todos os grupos musculares
    grupos.remove("Cárdio") #O Cárdio será tratado separadamente
    random.shuffle(grupos) #Embaralha a lista de grupos musculares

    estrategia = {dia: [] for dia in dias_semana} #Cria um dicionário para armazenar os treinos dos dias

    contagem = {grupo: 0 for grupo in grupos} #Contador para verificar quantas vezes um grupo foi escolhido

    #Para cada dia da semana
    for dia in dias_semana:
        #A lista de grupos disponíveis para o treino do dia, com base nos treinos que ainda não foram escolhidos duas vezes
        disponiveis = [g for g in grupos if contagem[g]<2 and not any(g in estrategia[d] for d in [dias_semana[dias_semana.index(dia)-1] if dias_semana.index(dia) > 0 else dia])]

        if len(disponiveis) >= 4: #Se houver pelo menos 4 grupos musculares disponíveis
            escolhidos = random.sample(disponiveis,4) #Escolhe aleatoriamente 4 grupos
            estrategia[dia].extend(escolhidos) #Adiciona os grupos ao treino do dia
            for g in escolhidos:
                contagem[g] += 1 #Marca que esse grupo foi escolhido

    return estrategia

def gerar_treino():
    estrategia_treino = gerar_estrategia() #Gera a estrategia dos treinos
    treino_semanal = {} #Cria o dicionário para armazenar os treinos de cada dia

    for i, dia in enumerate(dias_semana):
        treino_dia = {"Cárdio": [random.choice(exercicios["Cárdio"])]} #Escolhe um Cárdio para o dia
        for grupo in estrategia_treino[dia]:
            treino_dia[grupo] = random.sample(exercicios[grupo], 2) #Escolhe 2 exercícios para o grupo muscular
        treino_semanal[dia] = treino_dia #Adiciona o treino do dia ao treino semanal

    #Garantir que o sábado tenha 4 grupos musculares e que não repita grupos do dia anterior (sexta-feira)
    if dia == "Sábado":
        disponiveis = [g for g in list(exercicios.keys()) if g != "Cárdio" and g not in estrategia_treino["Sexta"]]
        escolhidos_sabado = random.sample(disponiveis, 4)
        for grupo in escolhidos_sabado:
            treino_dia[grupo] = random.sample(exercicios[grupo],2)

    return treino_semanal


def mostrar_treino():
    treino = gerar_treino()
    treino_texto = ""

    for dia, treino_dia in treino.items():
        treino_texto += f"{dia}:\n"
        for grupo, exercicios in treino_dia.items():
            treino_texto += f" {grupo}: {', '.join(exercicios)}\n"
        treino_texto += "\n"

    resultado_texto.delete(1.0,tk.END) #Limpar a área de texto
    resultado_texto.insert(tk.END,treino_texto) #Exibir o treino gerado

#Criando a interface gráfica
root = tk.Tk()
root.title("Automação de Treinos")

#Botão para gerar treino
gerar_button = tk.Button(root,text="Gerar Treino",command=mostrar_treino)
gerar_button.pack(pady=20)

#Área de texto para exibir o treino
resultado_texto = tk.Text(root,width=60,height=30)
resultado_texto.pack(pady=10)


root.mainloop()