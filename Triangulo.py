# La Aplicaciion calcula el area del trianguilo donde puide dos datos base 
# y altura loa calgulo y devyuelve el area del triangulo.

from http.server import HTTPServer , BaseHTTPRequestHandler
import urllib.parse
class LMCDPRequestHandler(BaseHTTPRequestHandler):

# Variable de tipo string que contien el html del lo que solicita el post para el calculo del triangulo
    html_calc_triangulo = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculador de Área de Triángulos de RM</title>
    </head>
    <body>
        <h1>Calculador de Área de Triángulos de RM</h1>

        <form action="/calcular_area" method="POST"> <label for="base">Base:</label>
            <input type="number" id="base" name="base" required>

            <label for="altura">Altura:</label>
            <input type="number" id="altura" name="altura" required>

            <button type="submit">Calcular</button>
        </form>
    </body>
    </html>
    """  

    def genera_resultado(self, base, altura):
        """ 
        calcula el area de ltriangulo
        Args: 
            base (float): es la base del triangulo. 
            altura (float): Es la altura que tieneel triangulo. 
            resultado (float): es el calculo de area del truangulo ( base * altura / 2 )
        Returns:             
            html_area: (string)  Devuelve una html con el resultado del calculo del triangulo.            
        Raises:   
            resultado (float): es el calculo de area del truangulo ( base * altura / 2 )          
            resultado (float): no me presenta error             
        """
        resultado = base * altura / 2
        html_area= f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Respuesta Calculador de Área de Triángulos de RM</title>
        </head>
        <body>
            <h1>Calculador de Área de Triángulos de RM</h1>
        
            <h3>El área de un triángulo de base {base} y altura {altura} es: {resultado}</h3>
        </body>
        </html>
        """
        return html_area

    def do_GET(self):
        """ 
        Maneja las peticiones GET verel calculo del triagulo. 
        Args: 
        request (HttpRequest):        
        Returns: 
          HttpResponse: 
            Una respuesta HTTP con un mensaje de saludo. 
        """

        print("------- Contenido del request SELF-------")
        print(f"path = {self.path}")
        for key, value in self.__dict__.items():
            print (f"Atributo de instancia ='{key}' contiene {value}")
        print("------- Final contenido -------")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(self.html_calc_triangulo, 'utf-8'))


    def do_POST(self):
        """ 
        Maneja las peticiones POST para la calclular el area del trineculo. 
        Args: 

        Returns: 
            HttpResponse: 
                resultado (float): base * altura / 2
        Raises: 
            ValueError:             
                genera_resultado(base, altura)                
        """

        print("------- Contenido del request POST -------")
        print(f"path = {self.path}")
        for key, value in self.__dict__.items():
            print (f"Atributo de instancia ='{key}' contiene {value}")
            
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        print(f"post data = {post_data}")
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))
        print(f"parametros ={params}")
                # Extract base and height
        base = float(params['base'][0])
        altura = float(params['altura'][0])
        print("------- Contenido del request -------")  

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        resp_html = self.genera_resultado(base, altura)
        self.wfile.write(bytes(resp_html, 'utf-8')) #self.genera_resultado(base, altura)


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, puerto=8000):
    server_address = ('localhost', puerto)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor levantado en http://localhost:{puerto}")
    httpd.serve_forever()

run(handler_class = LMCDPRequestHandler, puerto=8025) #8025