"""
This program translates AWA5.0 awatalk to binary and then to readable commands.
There is currently no differentiation between integers and awascii, so both are printed as decimals.
You'll still need the Awa5.0 documentation to understand the commands and translate the decimals to awascii.
have fun :3
- joworld 01.06.2024
"""

def main():

    global input # is needed for some reason
    awa_dict = {}
    awatalk__to_binary = {}
    binary__to_code = {}
    awatalk_to_x_position = 0  # updates position in awatalk_to_binary/ binary_to_code once the current binary code has been determined
    awa_counter = 0  # counts awa's / wa's
    last_binary_length = 0  # if last binary lenght == 6 -> check if binary takes argument
    takes_argument = False  # if true -> next awa_counter goes up to 8
    awatalk__to_binary[awatalk_to_x_position] = ''
    binary__to_code[awatalk_to_x_position] = ''

    print("Welcome to awa5.0 to text translator! \n"
          "The current version can not differ between integers and awascii and thereby prints both as decimals \n"
          "Please enter the entire Awatalk with the initial 'awa'")
    input = input("Enter awatalk: ")

    # filtering out non-awa characters plus the initial 'awa'
    whitelist = set('aw AW')
    filtered_input = ''.join(filter(whitelist.__contains__, input)).lower()
    filtered_input = filtered_input[3:len(filtered_input)]
    if filtered_input[0] == ' ':
        filtered_input = filtered_input[1:len(filtered_input)]
    print("cleaned: ",filtered_input)
    awa_dict = filtered_input.split(' ')
    print("separated: ",awa_dict)

    for awa in range(len(awa_dict)):
        if awa_dict[awa] == 'awa':
            awatalk__to_binary[awatalk_to_x_position] = awatalk__to_binary[awatalk_to_x_position]+'0'
            awa_counter += 1
        else:
            awatalk__to_binary[awatalk_to_x_position] = awatalk__to_binary[awatalk_to_x_position] + '0'
            awa_counter += 1
            for i in range((len(awa_dict[awa])-3)//2): # for every 'wa' in the awa
                if awa_counter == 5 and takes_argument == False:
                    # check if binary takes argument, then continue
                    binary__to_code[awatalk_to_x_position], takes_argument = binary_to_operator(awatalk__to_binary[awatalk_to_x_position]) # find the operator
                    awatalk_to_x_position += 1
                    awa_counter = 0
                    awatalk__to_binary[awatalk_to_x_position] = ''
                    binary__to_code[awatalk_to_x_position] = ''
                elif awa_counter == 8 and takes_argument == True:
                    binary__to_code[awatalk_to_x_position] = binary_to_num(awatalk__to_binary[awatalk_to_x_position]) # make decimal
                    takes_argument = False
                    awatalk_to_x_position += 1
                    awa_counter = 0
                    awatalk__to_binary[awatalk_to_x_position] = ''
                    binary__to_code[awatalk_to_x_position] = ''
                awatalk__to_binary[awatalk_to_x_position] = awatalk__to_binary[awatalk_to_x_position]+'1'
                awa_counter += 1

        if awa_counter == 5 and takes_argument == False:
            # check if binary takes argument, then continue
            binary__to_code[awatalk_to_x_position], takes_argument = binary_to_operator(
                awatalk__to_binary[awatalk_to_x_position])  # find the operator
            awatalk_to_x_position += 1
            awa_counter = 0
            awatalk__to_binary[awatalk_to_x_position] = ''
            binary__to_code[awatalk_to_x_position] = ''
        elif awa_counter == 8 and takes_argument == True:
            binary__to_code[awatalk_to_x_position] = binary_to_num(
                awatalk__to_binary[awatalk_to_x_position])  # make decimal
            takes_argument = False
            awatalk_to_x_position += 1
            awa_counter = 0
            awatalk__to_binary[awatalk_to_x_position] = ''
            binary__to_code[awatalk_to_x_position] = ''

    print("binary: ",awatalk__to_binary)
    print("code: ",binary__to_code.values())






def binary_to_operator(binary):
    takes_argument = False
    operator = ''
    match binary:
        case '00000':
            operator = 'nop' # no operation
        case '00001':
            operator = 'prn' # print
        case '00010':
            operator = 'pr1' # print number
        case '00011':
            operator = 'red' # read
        case '00100':
            operator = 'r3d' # read number
        case '00101':
            operator = 'blo' # blow
            takes_argument = True
        case '00110':
            operator = 'sbm' # submerge
            takes_argument = True
        case '00111':
            operator = 'pop' # pop
        case '01000':
            operator = 'dpl' # duplicate
        case '01001':
            operator = 'srn' # surround
            takes_argument = True
        case '01010':
            operator = 'mrg' # merge
        case '01011':
            operator = '4dd' # Add
        case '01100':
            operator = 'sub' # subtract
        case '01101':
            operator = 'mul' # multiply
        case '01110':
            operator = 'div' # divide
        case '01111':
            operator = 'cnt' # count
        case '10000':
            operator = 'lbl' # label
            takes_argument = True
        case '10001':
            operator = 'jmp' # jump
            takes_argument = True
        case '10010':
            operator = 'eql' # equal to
        case '10011':
            operator = 'lss' # less than
        case '10100':
            operator = 'gtr' # greater than
        case '11111':
            operator = 'trm' # terminate
        case _:
            operator = 'this should not exist' # no operation
    # print("operator: ",operator)
    # print("takes_argument: ",takes_argument)

    return operator, takes_argument

def binary_to_num(binary):
    return int(binary, 2)


if __name__ == '__main__':
    main()