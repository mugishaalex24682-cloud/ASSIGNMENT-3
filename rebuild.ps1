param([string]$Name = "backend-container", [string]$Tag = "backend-app:latest")
docker rm -f $Name 2>$null | Out-Null
docker build --load -t $Tag .
docker run -d --name $Name -p 8080:8080 --restart unless-stopped $Tag
Start-Sleep -Seconds 2
docker logs -f $Name
