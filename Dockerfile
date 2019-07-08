FROM python:3.7.3

RUN pip install genepattern-python pandas

COPY module/ /removeSamples/

