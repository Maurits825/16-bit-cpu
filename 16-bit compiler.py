codefile = open('code_16_bit.txt','r');

rawcode = list();
binarycode = list();
hexcode = list();
addrf = {};
labels = {};
opcode = {'ADDWF,w': '00000001', 'ADDWF,f': '10000001', 'ADDWL': '00010001',
          'SUBWF,w': '00000010', 'SUBWF,f': '10000010', 'SUBWL': '00010010',
          'MULWF,w': '00000011', 'MULWF,f': '10000011', 'MULWL': '00010011',
          'MUHWF,w': '00000100', 'MUHWF,f': '10000100', 'MUHWL': '00010100',
          'DIVWF,w': '00000101', 'DIVWF,f': '10000101', 'DIVWL': '00010101',
          'MODWF,w': '00000110', 'MODWF,f': '10000110', 'MODWL': '00010110',
          'ROLF': '00011010', 'RORF': '00011011', 'INCRF': '00011100', 'DECRF': '00011101',
          'BTSCF': '1111', 'BTSSF': '1110', 'BSF': '1101', 'BCF': '1100',
          'NANDWF,w': '00000111', 'NANDWF,f': '10000111', 'NANDWL': '00010111',
          'NORWF,w': '00001000', 'NORWF,f': '10001000', 'NORWL': '00011000',
          'XORWF,w': '00001001', 'XORWF,f': '10001001', 'XORWL': '00011001',
          'MOVLW': '00011110', 'MOVWF': '00011111', 'MOVFW': '00100000', 'MOVLF': '00100010',
          'GOTO': '00100001', 'RIN,1': '00001010', 'RIN,2': '10001010',
          'WOUTL,1': '00001011', 'WOUTL,2': '10001011', 'WOUTF,1': '00001100', 'WOUTF,2': '10001100'};

codeline = codefile.readlines();

i = 0;
for line in codeline:
    if '#' not in line:                             #remove comments
        splitline = codeline[i].rstrip().split();
        if splitline:                               #remove white space
            if '%' in line:                         #add f memory address names
                addrf[splitline[1]] = splitline[2].replace('0b', '');
            elif len(splitline) == 1:               #goto label
                labels[splitline[0]] = format(len(rawcode), '016b');
            elif 'BTS' in splitline[0]:             #Bit test
                BT = splitline[0].split(',');
                BT[1] = format(int(BT[1]), '04b') + splitline[1].replace('0b', '');
                rawcode.append(BT);
            elif ('BS' or 'BC') in splitline[0]:               #Bit set and clear
                BT = splitline[0].split(',');
                BT[1] = format(int(BT[1]), '04b') + splitline[1].replace('0b', '');
                rawcode.append(BT);
            elif '0b' in splitline[1]:              #literal values
                splitline[1] = splitline[1].replace('0b', '');
                rawcode.append(splitline);
            elif splitline[0] == 'GOTO':            #replace goto label with binary
                splitline[1] = labels[splitline[1]];
                rawcode.append(splitline);
            else:
                splitline[1] = addrf[splitline[1]]; #addr names
                rawcode.append(splitline);
    i = i + 1;
print 'Raw code:'
print rawcode;

i = 0;
for line in rawcode:
    binarycode.append(opcode[rawcode[i][0]] + rawcode[i][1]);
    i = i + 1;
#print binarycode;

i = 0;
for line in binarycode:
    hexcode.append('%06X' % int(binarycode[i],2));
    i = i + 1;
print 'Hex code:'
print hexcode;

i = 0;
Hexfile = open('hexcode_16_bit.txt', 'w');
Hexfile.write('v2.0 raw\n')
for line in hexcode:
    Hexfile.write(hexcode[i] + ' ');
    i = i + 1;

Hexfile.close();
codefile.close();
