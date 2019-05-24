package br.insper.robot19;

import java.util.Comparator;

public class ComparatorGulosa implements Comparator<Node> {

    public int compare(Node b1, Node b2) {

        return Integer.compare(b1.getHeuristic(), b2.getHeuristic());
    }
}
