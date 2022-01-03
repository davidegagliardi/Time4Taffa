# Time4Taffa
Receive daily menu from Taffa

## Todo
- ✅ Implement multi-language menu (en/fi/sv)
- ✅ Subscribe for daily menu
- ✅ Unsubscribe function
- ✅ Get menu manually

## Run bot

```
git clone https://github.com/davidegagliardi/Time4Taffa.git
cd Time4Taffa
docker build -t time4taffa .
docker run -it --rm -e TOKEN="YOUR-TOKEN" time4taffa
```
It's recommended to use -v option and mount "content.sqlite" database path to keep data after container deletion
