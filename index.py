import tkinter as tk
import random

#Grupos musculares e exercícios
exercicios = {
    'Peito': ['Crucifixo','Supino Sentado','Flexão de Braço','Flexão Declinada'],
    'Costas': ['Puxada Alta','Remada Baixa','Puxada Alta Triângulo','Remada Curvada'],
    'Perna': ['Extensora','Agachamento','Stiff','Panturilha'],
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

def gerar_treino():
    treino_semanal = {}

    for dia in dias_semana:
        treino_dia = {}

        #Inclui cárdio todos os dias
        treino_dia['Cárdio'] = [random.choice(exercicios['Cárdio'])]

        #Definir a ordem aleatória dos grupos musculares
        grupos_musculares = [grupo for grupo in exercicios.keys() if grupo != 'Cárdio']
        random.shuffle(grupos_musculares)

        #Preencher os treinos de musculação
        for grupo in grupos_musculares[:5]:
            treino_dia[grupo] = random.sample(exercicios[grupo],2)

        treino_semanal[dia] = treino_dia

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
resultado_texto = tk.Text(root,width=50,height=15)
resultado_texto.pack(pady=10)


root.mainloop()