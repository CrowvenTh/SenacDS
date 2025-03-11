class Playlist:
    def __init__(self):
        self.playlist = []

    def adicionarMusica(self):
        titulo = input("\n===| Insira o titulo: ").capitalize()
        artista = input("===| Insira o artista: ").capitalize()
        self.titulo = titulo
        self.artista = artista
        self.playlist.append({"Titulo":titulo, "Artista":artista})

    def listarMusicas(self):
        for i, playlists in enumerate(self.playlist, 1):
            titulos = playlists["Titulo"]
            artistas = playlists["Artista"]

            print(f"=======| MÚSICA {i} |=======")
            print(f"===| Música: {titulos}\n===| Artista: {artistas}\n==========================")
def Texto():
    print(f"\n=======| PLAYLIST |=======")

            
playlist1 = Playlist()
Texto()
playlist1.adicionarMusica()
playlist1.adicionarMusica()
playlist1.adicionarMusica()
playlist1.listarMusicas()