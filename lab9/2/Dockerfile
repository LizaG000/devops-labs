FROM mcr.microsoft.com/dotnet/sdk:9.0 as builder
WORKDIR /app

COPY App/ /app/
RUN dotnet publish -c Release -o ./publish

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS runtime
WORKDIR /app

COPY --from=builder /app/publish .

CMD ["dotnet", "App.dll"]