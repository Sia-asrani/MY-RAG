rag-muj/
│
├── data/
│   └── muj_handbook.pdf
│
├── parser/
│   ├── pdf_parser.py
│   ├── hierarchy_detector.py
│   └── chunker.py
│
├── output/
│   └── chunks.json
│
├── notebooks/
│
├── requirements.txt
│
└── main.py



after parsing + chunking:

chunks.json
 ↓
BGE Embedding Model
 ↓
Vector Generation
 ↓
Store Embeddings
 ↓
Manual Retrieval