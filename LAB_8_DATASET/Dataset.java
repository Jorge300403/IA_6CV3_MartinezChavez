import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Dataset {
    public static void main(String[] args) {
        // Ruta al archivo bezdekIris.data
        String filePath = "C:/Users/jorge/OneDrive/Documentos/JORGE/ESCOM/9_SEMESTRE/IA/LABORATORIO/8_DATASETS/iris/bezdekIris.data";

        // Nombres de las columnas según el dataset Iris
        String[] columnas = {"logitud sepalo en cm", "ancho sepalo en cm", "longitud petalo en cm", "ancho petalo en cm", "clase"};

        // Crear una matriz para almacenar los datos (150 filas y 5 columnas)
        String[][] data = new String[150][5];

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            int row = 0;

            while ((line = br.readLine()) != null && row < 150) {
                // Dividir la línea por comas y almacenar en la matriz
                String[] values = line.split(",");
                System.arraycopy(values, 0, data[row], 0, values.length);
                row++;
            }

            // Imprimir los nombres de las columnas
            for (String columna : columnas) {
                System.out.print(columna + "\t");
            }
            System.out.println();

            // Imprimir las primeras 5 filas para verificar
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    System.out.print(data[i][j] + "\t");
                }
                System.out.println();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
