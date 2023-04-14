import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] dy = {-1, -1, -1, 0, 1, 1, 1, 0, 0};
        int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1, 0};
        int answer = 0;
        char[][] matrix = new char[8][8];
        for (int i = 0; i < 8; i++) {
            matrix[i] = sc.nextLine().toCharArray();
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{7, 0});
        boolean[][] visited;

        while (!queue.isEmpty()) {
            if (answer == 1) break;
            int size = queue.size();
            visited = new boolean[8][8];

            while (size-- > 0) {
                int[] cur = queue.poll();
                int cy = cur[0];
                int cx = cur[1];
                if(matrix[cy][cx] == '#')
                    continue;
                if (cy == 0 && cx == 7) {
                    answer = 1;
                }
                for (int k = 0; k < 9; k++) {
                    int ny = cy + dy[k];
                    int nx = cx + dx[k];
                    if (ny < 0 || ny >= 8 || nx < 0 || nx >= 8) continue;
                    if (matrix[ny][nx] == '#' || visited[ny][nx]) continue;
                    queue.add(new int[]{ny, nx});
                    visited[ny][nx] = true;
                }
            }

            char[][] next_matrix = new char[8][8];
            for (int i = 0; i < 7; i++) {
                for (int j = 0; j < 8; j++) {
                    next_matrix[i + 1][j] = matrix[i][j];
                }
            }
            for (int j = 0; j < 8; j++)
                next_matrix[0][j] = '.';
            matrix = next_matrix;

        }
        System.out.println(answer);
    }
}