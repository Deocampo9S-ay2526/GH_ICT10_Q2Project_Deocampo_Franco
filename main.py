from pyscript import display, document


# runs when the button is clicked
def creator_info(event):
    document.getElementById('display').innerHTML = ''
    info = document.getElementById('creator_input').value
    display(f'Info: {info}', target='display')