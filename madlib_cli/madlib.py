import re

print('Welcom to madlib game, a functionality programe that takes multiple inputs')

def read_template(file_name):
    try:
        with open(file_name) as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError

def parse_template(content):
    try:
        stripped_content=re.sub(r"\{.*?\}","{}",content)
        content_in_curly_braces = re.findall('{(.+?)}',content)
        return stripped_content, tuple(content_in_curly_braces)
    except:
        return 'an error occured while tracing the curlies'

def inputs(content_in_curly_braces):
    user_inputs = []
    for i in range(len(content_in_curly_braces)):
        user_input=input(f'Please Enter {content_in_curly_braces[i]}: ')
        user_inputs.append(user_input)
    return user_inputs

def merge(file_content,user_inputs):
    file_content=re.sub(r"\{.*?\}","{}",file_content)
    return file_content.format(*user_inputs)


#print(merge(read_template('assets/dark_and_stormy_night_template.txt'),inputs(parse_template(read_template('assets/dark_and_stormy_night_template.txt')))))
