FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir .
EXPOSE 4229
CMD ["uvicorn", "piphi_network_philips_hue_direct.main:app", "--host", "0.0.0.0", "--port", "4229"]
