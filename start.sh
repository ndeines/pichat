#!/bin/bash
source .env
uvicorn backend.main:app --reload &
streamlit run frontend/app.py
