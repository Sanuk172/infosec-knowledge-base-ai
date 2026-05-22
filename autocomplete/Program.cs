using System;
using System.Collections.Generic;

namespace Autocomplete
{
    internal class AutocompleteTask
    {
        public static string FindFirstByPrefix(IReadOnlyList<string> entries, string searchPrefix)
        {
            var firstMatchPosition = LeftBorderTask.GetLeftBorderIndex(entries, searchPrefix, -1, entries.Count) + 1;
            if (firstMatchPosition < entries.Count &&
                entries[firstMatchPosition].StartsWith(searchPrefix, StringComparison.OrdinalIgnoreCase))
            {
                return entries[firstMatchPosition];
            }

            return null;
        }

        public static string[] GetTopByPrefix(IReadOnlyList<string> entries, string searchPrefix, int limit)
        {
            var startMatchIndex = LeftBorderTask.GetLeftBorderIndex(entries, searchPrefix, -1, entries.Count) + 1;
            var totalMatches = GetCountByPrefix(entries, searchPrefix);
            if (totalMatches <= 0)
                return Array.Empty<string>();

            if (limit > totalMatches)
                limit = totalMatches;

            var topMatches = new string[limit];
            for (var offset = 0; offset < limit; offset++)
                topMatches[offset] = entries[startMatchIndex + offset];

            return topMatches;
        }

        public static int GetCountByPrefix(IReadOnlyList<string> entries, string searchPrefix)
        {
            var leftBoundary = LeftBorderTask.GetLeftBorderIndex(entries, searchPrefix, -1, entries.Count);
            var rightBoundary = RightBorderTask.GetRightBorderIndex(entries, searchPrefix, -1, entries.Count);
            return rightBoundary - leftBoundary - 1;
        }
    }

}