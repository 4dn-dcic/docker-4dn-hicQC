#!/usr/bin/env cwl-runner

class: CommandLineTool

cwlVersion: v1.0

requirements:
- class: DockerRequirement
  dockerPull: "4dndcic/4dn-hicqc:v1"

- class: "InlineJavascriptRequirement"

inputs:
  hicfile:
   type: File
   inputBinding:
    position: 1

  chromsizes:
   type: File
   inputBinding:
    position: 2

  outdir:
   type: string
   inputBinding:
    position: 3
   default: "."

outputs:
  mcool_qc:
   type: File
   outputBinding:
    glob: "$(inputs.outdir + '/' + '*.json')"

baseCommand: ["run-hicQC.sh"]
