package br.insper.robot19;

import java.util.Comparator;

public class ComparatorA implements Comparator<Node> {

    public int compare(Node b1, Node b2) {

        float result1 = b1.getHeuristic() + b1.getPathCost();
        float result2 = b2.getHeuristic() + b2.getPathCost();

        return Float.compare(result1, result2);
    }
}
