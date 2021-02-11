from straw import straw
import numpy as np
import click
import json


@click.command()
@click.argument('infile')
@click.argument('chromsizes')
@click.argument('outdir')
@click.argument('filename')
def main(infile, chromsizes, outdir, filename):
    normvec = 'KR'
    with open(chromsizes) as opf:
        chromosomes = opf.readlines()

    names = [a_line.split('\t')[0] for a_line in chromosomes]
    chroms = [name[3:] for name in names]
    resolutions = [1000, 2000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000, 2500000, 5000000, 10000000]

    report_dict = {'failed_balancing': []}
    for res in resolutions:
        failing_res = []
        for chrom in chroms:
            result = straw(normvec, infile, chrom, chrom, "BP", res)
            # print(res)
            # print(len(result[2]))
            is_nan = np.isnan(result[2]).all()
            if is_nan:
                if not failing_res:
                    failing_res.append(str(res))
                failing_res.append('chr' + chrom)
        if failing_res:
            report_dict['failed_balancing'].append(';'.join(failing_res))

    outpath = outdir + '/' + filename + '.json'
    with open(outpath, 'w') as outfile:
        json.dump(report_dict, outfile, indent=2)


if __name__ == "__main__":
    main()
