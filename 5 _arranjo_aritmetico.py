def arithmetic_arranger(problems, show_answers=False):
    # Verifica se há mais do que 5 problems solicitados
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    results_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        result = str(eval(problem)) if show_answers else ""

        width = max(len(num1), len(num2)) + 2  # Largura mínima necessária
        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dashes_line.append("-" * width)
        results_line.append(result.rjust(width))

    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dashes_line),
    ])

    if show_answers:
        arranged_problems += "\n" + "    ".join(results_line)

    return arranged_problems

def format_problem(problem):
    """Adiciona espaços entre números e operadores manualmente."""
    formatted_problem = ""
    for char in problem:
        if char in "+-":  # Se for um operador, adiciona espaços antes e depois
            formatted_problem += f" {char} "
        else:
            formatted_problem += char
    return formatted_problem.strip()  # Remove espaços extras no início e no fim

# Entrada do usuário
user_input = input("Digite os problemas separados por vírgula (exemplo: 8+2, 45-10, 99+1): ")
problems = [format_problem(problem.strip()) for problem in user_input.split(",")]

# Mostrar respostas? (S/N)
show_answers_input = input("Deseja mostrar as respostas? (s/n): ").strip().lower()
show_answers = show_answers_input == "s"

# Exibir resultado
print(f'\n{arithmetic_arranger(problems, show_answers)}')

