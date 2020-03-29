#import validate base
fileHandle1=open(r'C:\Users\dulanka\Documents\BIPython\validateBaseSequence.py').read()
exec(fileHandle1)

def gc_content(base_seq):
    print("calling function to validate sequence....\n")
    validateSeqRslt=validate_base_sequence(base_seq)
    print(validateSeqRslt)
    seq=base_seq.upper()
    return (seq.count('G')+seq.count('C'))/len(seq)
