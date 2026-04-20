#!/bin/bash
cd src && uvicorn omnimesh_x.deployment.api_server:app --reload --port 8000
