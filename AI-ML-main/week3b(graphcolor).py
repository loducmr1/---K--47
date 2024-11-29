colors=['pink','yellow','black']
states=['andhra','karnataka','tamilnadu','kerala']
neighbours={}
neighbours['andhra']=['karnataka','tamilnadu']
neighbours['karnataka']=['andhra','tamilnadu','kerala']
neighbours['tamilnadu']=['andhra','karnataka','kerala']
neighbours['kerala']=['karnataka','tamilnadu']
colors_of_states={}
def promising(state,color):
    for neighbour in neighbours.get(state):
        color_of_neighbour=colors_of_states.get(neighbour)
        if color_of_neighbour==color:
            return False
    return True
def get_color_for_state(state):
    for color in colors:
        if promising(state,color):
            return color
def main():
    for state in states:
      colors_of_states[state]=get_color_for_state(state)
    print(colors_of_states)
main()
