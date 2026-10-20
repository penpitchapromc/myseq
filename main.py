from argparse import ArgumentParser

from seqbio.calculation.SeqCal import gcContent, countBasesDict
from seqbio.pattern.SeqPattern import enzTargetsScan
from seqbio.seqMan.dnaconvert import reverseComplementSeq, dna2rna, dna2protein


def argparserLocal():
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    gc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    gc_command.add_argument("-s", "--seq", type=str, default=None,
                            help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                               help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action='store_true',
                               help="Convet DNA to reverse-complementary")

    trans_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    trans_command.add_argument("-s", "--seq", type=str, default=None,
                               help="Provide sequence")
    trans_command.add_argument("-r", "--revcomp", action='store_true',
                               help="Convet DNA to reverse-complementary")

    transl_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    transl_command.add_argument("-s", "--seq", type=str, default=None,
                                help="Provide sequence")
    transl_command.add_argument("-r", "--revcomp", action='store_true',
                                help="Convet DNA to reverse-complementary")

    enz_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enz_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enz_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")
    enz_command.add_argument("-r", "--revcomp", action='store_true',
                             help="Convet DNA to reverse-complementary")
    return parser


def main():
    parser = argparserLocal()
    args = parser.parse_args()

    seq = args.seq.upper()
    if args.command != 'gcContent' and args.revcomp:
        seq = reverseComplementSeq(seq)

    if args.command == 'gcContent':
        print("Input", args.seq, "\nGC content =", gcContent(seq))
    elif args.command == 'countBases':
        print("Input", args.seq, "\ncountBases =", countBasesDict(seq))
    elif args.command == 'transcription':
        print("Input", args.seq, "\nTranscription =", dna2rna(seq))
    elif args.command == 'translation':
        print("Input", args.seq, "\nTranslation =", dna2protein(seq))
    elif args.command == 'enzTargetsScan':
        print("Input", args.seq, "\n" + args.enz, "sites =", enzTargetsScan(seq, args.enz))


if __name__ == "__main__":
    main()