import argparse

def build_parser():
    parser = argparse.ArgumentParser()

    # Input Options
    parser.add_argument('--style', type=str, dest='style', help='style image path',
                        default='./examples/style/01.png')

    parser.add_argument('--batch_size', type=int, dest='batch_size', help='batch size',
                        default=2)
    parser.add_argument('--max_iter', type=int, dest='max_iter', help='max iterations',
                        default=2e4)

    parser.add_argument('--learning_rate', type=float, dest='learning_rate',
                        default=1e-3)
    parser.add_argument('--iter_print', type=int, dest='iter_print', default=5e2)

    parser.add_argument('--checkpoint_iterations', type=int, dest='checkpoint_iterations',
                        help='checkpoint frequency', default=1e3)
    parser.add_argument('--train_path', type=str, dest='train_path',
                        help='path to training content images folder', default="./data/MSCOCO")

    # Weight Options
    parser.add_argument('--content_weight', type=float, dest="content_weight",
                        help='content weight (default %(default)s)', default=80)
    parser.add_argument('--style_weight', type=float, dest="style_weight",
                        help='style weight (default %(default)s)', default=1e2)
    parser.add_argument('--tv_weight', type=float, dest="tv_weight",
                        help="total variation regularization weight (default %(default)s)",
                        default=2e2)

    # Finetune Options
    parser.add_argument('--continue_train', type=bool, dest='continue_train', default=False)

    # Others
    parser.add_argument('--sample_path', type=str, dest="sample_path",
                        default='./examples/content/01.jpg')

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

