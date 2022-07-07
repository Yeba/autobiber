# Autobiber: A tool to find bibs via dblp

Find and reformat bib via `https://dblp.org/search/publ/api?h=1000&q="`


## Installation
````
pip install autobiber
````

Or
````
git clone https://github.com/Yeba/autobiber.git
cd autobiber/
pip install -e .
````

## Usage

```bash
autobiber -i input.bib -o output.bib
autobiber -i list.txt -o output.bib
autobiber -t "this is a title"
```

## Input File
txt:
````txt
attention is all you need
node2vec: node2vec: Scalable Feature Learning for Networks
````
We accept two formats in txt:
- title
- nickname:title

Note that, if ":" in title, it will be regraded as nickname, so add nickname manually.

bib:
````bib
@{attention,
title={attention is all you need}
}
````

More information is welcome, but only title is used while matching right now.

## Output
If more than one bib is found, "xxx find many, please choose manually" will be printed.
All bib matched wil be saved.
 ```
 @inproceedings{attentionisallyouneed,
  author    = {Ashish Vaswani and
               Noam Shazeer and
               Niki Parmar and
               Jakob Uszkoreit and
               Llion Jones and
               Aidan N. Gomez and
               Lukasz Kaiser and
               Illia Polosukhin},
  editor    = {Isabelle Guyon and
               Ulrike von Luxburg and
               Samy Bengio and
               Hanna M. Wallach and
               Rob Fergus and
               S. V. N. Vishwanathan and
               Roman Garnett},
  title     = {Attention is All you Need},
  booktitle = {Advances in Neural Information Processing Systems 30: Annual Conference
               on Neural Information Processing Systems 2017, December 4-9, 2017,
               Long Beach, CA, {USA}},
  pages     = {5998--6008},
  year      = {2017},
  url       = {https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html},
  timestamp = {Thu, 21 Jan 2021 15:15:21 +0100},
  biburl    = {https://dblp.org/rec/conf/nips/VaswaniSPUJGKP17.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}


@article{attentionisallyouneed,
  author    = {Ashish Vaswani and
               Noam Shazeer and
               Niki Parmar and
               Jakob Uszkoreit and
               Llion Jones and
               Aidan N. Gomez and
               Lukasz Kaiser and
               Illia Polosukhin},
  title     = {Attention Is All You Need},
  journal   = {CoRR},
  volume    = {abs/1706.03762},
  year      = {2017},
  url       = {http://arxiv.org/abs/1706.03762},
  eprinttype = {arXiv},
  eprint    = {1706.03762},
  timestamp = {Sat, 23 Jan 2021 01:20:40 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/VaswaniSPUJGKP17.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

 ```

## Supported Conferences and Articles
Every conference and article since you can find in vdlp.


## One more thing
Welcome PR.

Please email yjliu045@stu.suda.edu.cn or create Github issues here if you have any questions or suggestions.

